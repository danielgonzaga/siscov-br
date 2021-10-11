import { Component, EventEmitter, OnInit, Output } from '@angular/core';

@Component({
  selector: 'app-sergipe',
  templateUrl: './sergipe.component.html',
  styleUrls: ['./sergipe.component.css']
})
export class SergipeComponent implements OnInit {

  @Output() clickedLocal = new EventEmitter;

  constructor() { }

  ngOnInit(): void {}

  getLocal(event) {
    this.clickedLocal.emit(event);
  }

}
