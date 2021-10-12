import { Component, EventEmitter, OnInit, Output } from '@angular/core';

@Component({
  selector: 'app-amazonas',
  templateUrl: './amazonas.component.html',
  styleUrls: ['./amazonas.component.css']
})
export class AmazonasComponent implements OnInit {

  @Output() clickedLocal = new EventEmitter;

  constructor() { }

  ngOnInit(): void {}

  getLocal(event) {
    this.clickedLocal.emit(event);
  }

}
