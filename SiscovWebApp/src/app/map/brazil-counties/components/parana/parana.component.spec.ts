import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ParanaComponent } from './parana.component';

describe('ParanaComponent', () => {
  let component: ParanaComponent;
  let fixture: ComponentFixture<ParanaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ParanaComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ParanaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
