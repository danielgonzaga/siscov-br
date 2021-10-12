import { Component, EventEmitter, OnInit, Output } from '@angular/core';

@Component({
  selector: 'app-roraima',
  templateUrl: './roraima.component.html',
  styleUrls: ['./roraima.component.css']
})
export class RoraimaComponent implements OnInit {

  @Output() clickedLocal = new EventEmitter;

  constructor() { }

  ngOnInit(): void {}

  getLocal(event) {
    this.clickedLocal.emit(event);
  }

}
